import $ from 'jquery'
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css'

$(document).ready(function () {
	$('a.nav-link').on('click', function (event) {
		if (this.hash !== '') {
			event.preventDefault()
			var hash = this.hash
			$('html, body').animate(
				{
					scrollTop: $(hash).offset().top,
				},
				800,
				function () {
					window.location.hash = hash
				}
			)
		}
	})
})

$(document).ready(function () {
	$('#process-button').on('click', function () {
		var inputText = $('#input-textarea').val()
		$.ajax({
			type: 'POST',
			url: 'http://localhost:5000/process_vacancy',
			data: JSON.stringify({ description: inputText }),
			contentType: 'application/json',
			dataType: 'json',
			success: function (response) {
				$('#output-container').html(
					'<p class="output-text">' + response + '</p>'
				)
			},
			error: function () {
				$('#output-container').html(
					'<p class="output-text">Ошибка при обработке текста</p>'
				)
			},
		})
	})
})
