from flask import url_for, redirect, render_template, request
from flask_login import current_user, login_required
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import private_config
from tests import bp
from undyingkingdoms import app
from undyingkingdoms.models.forms.activate import EmailVerificationForm


@app.route('/activate/', methods=['GET', 'POST'])
@login_required
def activate():
    form = EmailVerificationForm()
    user = current_user
    if request.method == "POST":
        if form.validate_on_submit():
            if user.verify_verification_hash(form.code.data.strip()):
                user.is_verified = True
                user.save()
                return redirect(url_for('initialize'))
        return redirect(url_for('activate'))

    # TODO: make this only send once unless user request resend.
    # TODO: hash should be different every time.

    email_hash = user.generate_verification_hash()

    user_name = user.username
    user_email = user.email

    from_email = "Undying Kingdoms <no-reply@undyingkingdoms.com>"
    subject = 'Welcome to Undying Kingdoms'
    to_email = f"{user_name} <{user_email}>"
    content = render_template(
        'email/activate_body.html',
        user_name=user_name,
        email_hash=email_hash,
    )

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    print(message)

    try:
        sg = SendGridAPIClient(api_key=private_config.SENDGRID_API_KEY)
        # noinspection PyUnresolvedReferences
        response = sg.send(message)
        assert response.status_code == 202
    except Exception as e:
        print(e, message)
    return render_template(
        'index/activate.html',
        form=form,
        user=user
    )
