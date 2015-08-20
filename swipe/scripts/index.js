$(function () {
	var content = $('#content')
	var hammer = new Hammer(content.get(0))
	
	hammer.on('swipe', function (ev) {
		$('#content').dragend('left')
	})

	$('#content').dragend()
	
	$('.left').click(function () {
		$('#content').dragend('left')
	})
	
	$('.right').click(function () {
		$('#content').dragend('right')
	})
})