/**
 * Created by ajmal on 15/4/17.
 */
angular.module('suraksha').controller('homeControl',function ($scope,QuizService,$rootScope,$state) {
    $scope.city = '';
    $scope.age = 1;
    $scope.gender = 'unspecified';

    $scope.next = function () {
        $rootScope.loading = true;
        QuizService.setUserDetails($scope.city.toLowerCase(),$scope.age,$scope.gender).then(function () {
            $rootScope.loading = false;
            $state.go('story');
        },function () {
            $rootScope.loading = false;
            alert('Server Error');
        });
    }
});