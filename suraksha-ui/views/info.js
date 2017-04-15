/**
 * Created by moonlace on 14/04/17.
 */
angular.module('suraksha').controller('infoControl',function ($scope, QuizService,$state) {
	$scope.description = QuizService.getCurrentQuestion().desc;
	$scope.imageUrl = QuizService.getCurrentQuestion().correctAnswerUrl;
	$scope.answerStatus = QuizService.getAnswerStatus();

	$scope.playAudio = function() {
    	if($scope.answerStatus == 'correct'){
            var audio = new Audio('audio/Correct-answer.mp3');
        }else{
            var audio = new Audio('audio/Correct-answer.mp3');
		}
        audio.play();
    };
    $scope.playAudio();

	$scope.next = function () {
		QuizService.nextQuestion();
    };

	$scope.$on('QUESTION:ready',function () {
		$state.go('question');
    });

	$scope.$on('LEVELCHANGE',function () {
		$state.go('levelDesc');
    });

	$scope.$on('QUIZFINISHED',function () {
        $state.go('score');
    });
});