$(document).ready(function() {
	var converter = new showdown.Converter();
	converter.setOption('noHeaderId', true)
	converter.setOption('headerLevelStart', 4)
	var text = $('#text');
	var html = converter.makeHtml(text.html());
	text.html(html);
	//DOMPurify.sanitize(text.html());
});