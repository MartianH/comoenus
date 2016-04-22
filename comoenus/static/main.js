$(document).ready(function() {
	var loginA = $('#login-a');
	var signupA = $('#signup-a');
	var formLoginBtn = $('#lgn-btn');
	var form = $('#login-form');
	var submitCont = typeof $('#submit-cont') !== 'undefined';


	loginA.click(function(e) {
		e.preventDefault();
		loginA.fadeOut(100).delay(10000, function() {
			$('#login-form').fadeIn(500);
		});
	});

	signupA.click(function(event) {
		swal.withForm({
		    title: 'Sign Up',
		    showCancelButton: true,
		    confirmButtonColor: 'black',
		    confirmButtonText: 'register',
		    closeOnConfirm: true,
		    formFields: [
		        { id: 'uname', placeholder:'Username' },
		        { id: 'email', placeholder:'E-mail' },
		        { id: 'pswd', placeholder:'Password' },
		        { id: 're-pswd', placeholder:'Password' }
		    ]
		}, function(isConfirm) {
			if (isConfirm) {
				// do whatever you want with the form data
			    data = JSON.stringify(this.swalForm);
			    console.log(data)
			    $.ajax({
				url: '/signup',
				type: 'POST',
				contentType: "application/json; charset=utf-8",
				data: data,
				})
				.done(function(res) {
					//location.reload();
					console.log(res.message)

				})
				.fail(function(err) {
					console.log(err.responseText)
				})
			}
		})
	});

	form.submit(function(e) {
		var errText = $('#err-text');
		$.ajax({
			url: '/login',
			type: 'POST',
			data: form.serialize(),
		})
		.done(function(res) {
			location.reload();

		})
		.fail(function(err) {
			console.log(err.responseText)
			errText.html(err.responseText);
			errText.fadeIn('500').delay(2000).fadeOut('500');
		})
		e.preventDefault();
	});

	if (submitCont) {
		var inputTitle = $('#input-title');
		var inputArea = $('#input-area');
		var counter = null;

		inputTitle.on('input blur', function() {
			if (inputTitle.val().length == 0) {
				console.log('Data');
				inputTitle.css('border-color', 'red');
			}
			else {
				inputTitle.css('border-color', 'black');
			}
		});
		inputArea.on('input', function(event) {
			String.prototype.countWords = function(){
			  return this.split(/\s+/).length;
			}
			counter = inputArea.val().countWords();
			if (counter <= 1) {
				$('#word-count').html(counter + ' word');
			}
			else {
				$('#word-count').html(counter + ' words');
			}
			console.log(inputArea.val().length)
			if (inputArea.val().length != 0 && counter >= 10) {
				$('#form-submit-btn').fadeIn('500');
			}
			else {
				$('#form-submit-btn').fadeOut('300');
			}
		});

	}
	
});