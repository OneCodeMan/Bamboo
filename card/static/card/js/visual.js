$hidedeck = $("#hidedeck");
$decks = $(".deckrow");
$hidequiz = $("#hidequiz");
$quizzes = $(".quizrow");

// toggle text
$.fn.extend({
	toggleText: function(a, b) {
		return this.text(this.text() == b ? a : b);
	}
});

$hidedeck.on('click', function() {
	$decks.toggle("slow");
	$(this).toggleText('hide decks', 'show decks')
});

$hidequiz.on('click', function() {
	$quizzes.toggle("slow");
	$(this).toggleText('hide quizzes', 'show quizzes')
});

// randomize greet
$greet = $("#greet");
$compliment = $("#compliment");
greetings = ["Hello", "Hi", "Welcome", "Yo"];
compliments = ["Nice to see you again!", "Have a great time studying!", "We hope you have a great time studying :)"];
rand_greet = Math.floor(Math.random() * greetings.length);
rand_compliment = Math.floor(Math.random() * compliments.length);

$greet.text(greetings[rand_greet]);
$compliment.text(compliments[rand_compliment])


$hideterms = $("#hideterms");
$hidedefinitions = $("#hidedefinitions");
$cardterm = $(".cardterm");
$carddefinition = $(".cardefinition");

$hideterms.on('click', function() {
	$cardterm.toggleClass("blacken");
	$(this).toggleText('hide terms', 'show terms');
})

$hidedefinitions.on('click', function() {
	$carddefinition.toggleClass("blacken");
	$(this).toggleText('hide definitions', 'show definitions');
})