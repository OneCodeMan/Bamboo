$username_field = $("#id_username");
var window_checker = false;

function callAjax (url, method, callback, post) {
	var xmlhttp;
	post = post || '';
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			callback(xmlhttp.responseText);
		}// if
	}
	if (method == 'GET') {
		xmlhttp.open('GET', url, true);
		xmlhttp.send();
	}// if

	else if (method == 'POST') {
		xmlhttp.open("POST", url, true);
		xmlhttp.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
		xmlhttp.setRequestHeader('X-CSRFToken', docCookies.getItem('csrftoken'));
		xmlhttp.send(post);
	} //elif
}

function username_checker() {
	if (document.getElementById('id_username').value && !window.checker_busy) {
		window.checker_busy = true;
		console.log('function called')
		callAjax('{{ url_check_username }}?username='+document.getElementById('id_username').value, 'GET', username_checker_src); 
	}

}

function username_checker_src(src) {
	console.log('function called');
	document.getElementById('id_username_checker').next_src = src;
	setTimeout("document.getElementById('id_username_checker').src = document.getElementById('id_username_checker').next_src; window.checker_busy = false;", 1000);
}

$username_field.keypress(function() {
	username_checker();
})