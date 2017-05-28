/*jslint browser: true*/
/*global $, jQuery, alert*/

$(function () {
	"use strict";
	$('#btnSignUp').click(function () {
	
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function (response) {
				console.log(response);
				window.location = "/signInNew"
			},
			error: function (error) {
				console.log(error);
			}
		});
	});
});