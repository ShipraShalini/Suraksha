/**
 * Created by ajmal on 15/4/17.
 */
angular.module('suraksha').controller('scoreControl',function ($scope, QuizService) {
    $scope.score = QuizService.getScore();
    $scope.totalScore = QuizService.getTotalScore();
});