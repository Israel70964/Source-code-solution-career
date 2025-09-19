document.addEventListener('DOMContentLoaded', function() {
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                subject: document.getElementById('subject').value,
                message: document.getElementById('message').value
            };
            
            fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                const messageDiv = document.getElementById('formMessage');
                if (data.status === 'success') {
                    messageDiv.innerHTML = '<div class="alert alert-success">' + data.message + '</div>';
                    contactForm.reset();
                } else {
                    messageDiv.innerHTML = '<div class="alert alert-danger">There was an error sending your message. Please try again.</div>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                const messageDiv = document.getElementById('formMessage');
                messageDiv.innerHTML = '<div class="alert alert-danger">There was an error sending your message. Please try again.</div>';
            });
        });
    }
});