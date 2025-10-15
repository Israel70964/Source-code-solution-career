from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/careers')
def careers():
    # Sample career listings
    jobs = [
        {
            'title': 'Software Engineer',
            'department': 'Engineering',
            'location': 'Remote',
            'type': 'Full-time',
            'description': 'Join our engineering team to build amazing products.'
        },
        {
            'title': 'Product Manager',
            'department': 'Product',
            'location': 'San Francisco, CA',
            'type': 'Full-time',
            'description': 'Lead product strategy and work with cross-functional teams.'
        },
        {
            'title': 'UX Designer',
            'department': 'Design',
            'location': 'New York, NY',
            'type': 'Full-time',
            'description': 'Create beautiful and intuitive user experiences.'
        }
    ]
    return render_template('careers.html', jobs=jobs)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    # In a real application, you would save this to a database
    # For now, just return a success response
    return jsonify({'status': 'successful', 'message': 'Thank you for your message!'})

if __name__ == '__main__':
    # Configure for Replit environment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
