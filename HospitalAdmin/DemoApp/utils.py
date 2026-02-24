# import os
# import subprocess
# from django.conf import settings

# def save_invoice_as_image(html_content):
#     # Write HTML content to a temporary file
#     with open('temp_invoice.html', 'w') as f:
#         f.write(html_content)

#     # Define the output path for the image inside the static/image folder
#     output_path = os.path.join(settings.STATIC_ROOT, 'image', 'invoice.png')

#     # Convert HTML to image using wkhtmltoimage
#     subprocess.run(['wkhtmltoimage', 'temp_invoice.html', output_path])

#     # Remove the temporary HTML file
#     os.remove('temp_invoice.html')

#     return output_path
