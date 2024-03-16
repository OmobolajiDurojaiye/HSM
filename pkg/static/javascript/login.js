$(document).ready(function() {
    $('#serviceprovider_loginForm').hide();

    $('#serviceprovider').click(function() {
        $('#serviceprovider_loginForm').show();
        $('#customer_loginForm').hide();
    });

    $('#customer').click(function() {
        $('#customer_loginForm').show();
        $('#serviceprovider_loginForm').hide();
    });

    //customer form validation
    $('#customersubmit').click(function() {
        customeremail = $('#customeremail').val()
        customerpwd = $('#customerpwd').val()

        if (customeremail == '' || customerpwd == '') {
            $('#customererror').text('No field should be left empty!')
        }
    });

    //serviceprovider form validation
    $('#serviceprovidersubmit').click(function() {
        serviceprovideremail = $('#serviceprovideremail').val()
        serviceproviderpwd = $('#serviceproviderpwd').val()

        if (serviceprovideremail == '' || serviceproviderpwd == '') {
            $('#serviceprovidererror').text('No field should be left empty!')
        }
    });
});