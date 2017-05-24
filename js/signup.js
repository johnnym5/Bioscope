$(document).ready(function () {
	
	$('#signup-form').validate({
		rules: {
			fn: {
				required : true
			},
			ln: {
				required : true
			},
			em: {
				required : true
			},
			pwd: {
				required : true
			},
			cc: {
				required : true
			}
		},
		
		highlight: function (element) {
			$(element).closest('.form-group').removeClass('success').addClass('error');
		},
		
		success: function (element) {
			element.text('OK!').addClass('valid')
            .closest('.form-group').removeClass('error').addClass('success');
		}
	});
});