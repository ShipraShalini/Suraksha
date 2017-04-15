angular.module('suraksha').controller('storyControl',function ($scope,QuizService,$state,$rootScope) {
    $rootScope.loading = true;
    console.log('Story JS');
    $scope.selectedOption = '';
    QuizService.initialise().then(function (result) {
        $scope.subjects = result;
        $rootScope.loading = false;
    },function () {
        $rootScope.loading = false;
        alert('Server Error');
        $state.go('home');
    });

    $scope.next = function () {
        if($scope.selectedOption != null){
            $rootScope.loading = true;
            QuizService.beginLevel($scope.selectedOption).then(function (result) {
                $state.go('levelDesc');
                $rootScope.loading = false;
            });
        }else{
            $rootScope.loading = false;
            alert('Select Subject');
        }
    }
});