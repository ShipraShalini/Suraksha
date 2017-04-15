/**
 * Created by moonlace on 14/04/17.
 */
angular.module('suraksha').controller('questionControl',function ($scope,$rootScope,QuizService,$filter,$state) {
    $scope.question = QuizService.getCurrentQuestion();
    console.log($scope.question);
    $scope.options = [
        {
            optionId: 0,
            optionText: $scope.question.correctAnswer,
            optionUrl: $scope.question.correctAnswerUrl
        },
        {
            optionId: 1,
            optionText: $scope.question.wrongAnswer1,
            optionUrl: $scope.question.wrongAnswer1Url
        },
        {
            optionId: 2,
            optionText: $scope.question.wrongAnswer2,
            optionUrl: $scope.question.wrongAnswer2Url
        },
        {
            optionId: 3,
            optionText: $scope.question.wrongAnswer3,
            optionUrl: $scope.question.wrongAnswer3Url
        }
    ];
    $scope.selectedOption = JSON.stringify($scope.options[2]);
    $scope.options = $filter('orderBy')($scope.options,'-optionText');

    $scope.submit = function () {
        console.log(JSON.parse($scope.selectedOption));
        $rootScope.$broadcast('USERRESPONSE',{id:$scope.question.id, response: JSON.parse($scope.selectedOption).optionId});
        $state.go('info');
    };

});