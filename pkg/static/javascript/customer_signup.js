$(document).ready(function() {
    $('#signup-customer').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/image',
            type: 'GET',
            success: function(response) {
                var imageUrl = response.image2;
                
                $('#content').html(`
                    <div class="contact-container">

                        <div class="contact-container-head">
                            <h1>
                                Look For Home Services
                            </h1>
                            <p>
                               Fill in your information to look for home services!
                            </p>
                        </div>
                        
                        <div class="contact-container-body">
                            <div class="contact-form">
                               <form style="padding: 5%;" id="contact-form" action="/index" method="post">
                                    <input type="hidden" name="csrf_token" value="{{csrf_token()}}">
                                    
                                    <input type="text" name="username" id="username" placeholder="Your Name" autocomplete=true required>
                                    <input type="email" name="email" id="email" placeholder="Your Email" autocomplete=true required>
                                    <input type="password" name="password" id="password" placeholder="*****" required>
                                    <input type="submit" value="Sign Up">
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

        $.ajax({
            url: '/index',
            type: 'POST',
            data: {
                name: $('#name').val(),
                email: $('#email').val(),
                password: $('#password').val(),
                data: "{{csrf_token()}}",
            },
            success: function(response) {
                if (response.success) {
                    alert('Message sent successfully!');
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(error) {
                alert('An error occurred while sending the message.');
            }
        });        
    });

});