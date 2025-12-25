import asyncio

async def send_welcome_email(email : str):

    print(f"Sending welcome email to {email}")

    await asyncio.sleep(5)

    print(f"Welcome email sent to {email}")