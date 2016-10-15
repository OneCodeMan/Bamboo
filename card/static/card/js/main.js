$username_field = $("#id_username");

$(document).ready(function() {

	$username_field.keypress(function() {
		$.ajax({
			type: "POST",
			url: "/ajax/check_username",
			dataType: "json",
			data: { 
				csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').first().val(),
				"user": $("username_field").val()
			 },
			success: function(data) {
				if (data.is_taken) {
					alert(data.error_message);
				}//if
			},//function
			error: function(request, error) {
				console.log(error);
			}
		});//success
	});// keypress

// security csrf stuff
	function getCookie(name) {
		var cookieValue = null;
		var i = 0;

		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (i; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);

				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}// if
			}//for
		}//if

	return cookieValue;

	}//func

	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
		crossDomain: false,
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}// if
		}// beforeSend
	});// ajaxSetup

}); // document
