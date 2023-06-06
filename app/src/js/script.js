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
		findWords()
	})
}) 


$(document).ready(function () {
	$('#process-url-button').on('click', function () {
		findWords()
	})
})


$(document).ready(function () {
	document.querySelector('textarea').addEventListener('keydown', (e) => {
		if (e.key === 'Enter' && !event.shiftKey) {
		e.preventDefault()
		findWords()
		return
		}
	})
})


function findWords(){
	alert()
	var inputText = $('#input-url-textarea').val()
		$.ajax({
			type: 'POST',
			url:
				process.env.NODE_ENV === 'production'
					? 'https://aihunter.ru/agw/process_vacancy_by_url'
					: 'http://localhost:5000/process_vacancy_by_url',
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
}