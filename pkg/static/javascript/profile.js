$(document).ready(function(){
    $('#profile').click(function(e) {
        e.preventDefault();
        $('#content').html(`
            <div class="head">
                <div class="welcome-text">
                    <h1>
                        Hello, Omotola <span>Customer</span>
                    </h1>
                    <a href="" class="btn-sm">Log Out</a>
                </div>

                <div class="profile-pic">
                    <img src="{{url_for('static', filename='images/welcome-image (3).png')}}" alt="">
                </div>
            </div>
        `);
    })
})