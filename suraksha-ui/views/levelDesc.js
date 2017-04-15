  angular.module('suraksha').controller('levelDescControl',function ($scope,QuizService) {
    $scope.description = QuizService.getCurrentLevelData().level_desc;
    $scope.playAudio = function () {
        var audio = new Audio('audio/transition.wav');
        audio.play();
    };
    $scope.playAudio();
});