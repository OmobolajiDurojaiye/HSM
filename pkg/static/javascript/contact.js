$(document).ready(function() {
    $('#contact-link').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/image',
            type: 'GET',
            success: function(response) {
                var imageUrl = response.image;
                
                $('#content').html(`
                    <div class="contact-container">
                        <div class="contact-container-head">
                            <h1>
                                Have Questions? Contact Us
                            </h1>
                            <p>
                                Don't hesitate to contact us with any inquiries or feedback. 
                                We're committed to providing excellent customer service and are eager to assist you.
                            </p>
                        </div>

                        <div class="contact-container-body">
                            <div class="contact-form">
                                <form id="contact-form" action="/index" method="post">
                                    
                                    
                                    <input type="text" name="name" id="name" placeholder="Your Name" autocomplete=true required>
                                    <input type="email" name="email" id="email" placeholder="Your Email" autocomplete=true required>
                                    <textarea name="message" id="message" placeholder="Your Message" autocomplete=true required></textarea>
                                    <input type="submit" value="Send Message">
                                </form>
                            </div>

                            <div class="contact-image">
                                <img src="${imageUrl}" alt="">
                            </div>
                        </div>
                    </div>
                `);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $(document).on('submit', '#contact-form', function(e) {
        e.preventDefault();
    
        // Retrieve CSRF token from the meta tag
        var csrfToken = $('meta[name=csrf-token]').attr('content');
    
        $.ajax({
            url: '/index',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: $('#contact-form').serialize(),
            success: function(response) {
                if (response.success) {
                    alert('Message sent successfully!');
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(error) {
                alert('Error: ' + error);
            }
        });        
    });    
});
