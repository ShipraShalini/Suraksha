/**
 * Created by moonlace on 14/04/17.
 */
var suraksha = angular.module('suraksha', [
    'ui.router'
]);

suraksha.run(function ($rootScope) {
    console.log('App initialise');
    $rootScope.baseURL = 'http://localhost:8000/';
    // $rootScope.baseURL = 'http://172.20.10.4:8000/';
});

suraksha.config(function ($stateProvider) {
    $stateProvider

        .state('home',
            {
                url: '/',
                templateUrl: "./views/home.html",
                controller: 'homeControl'
            })
        .state('story',
            {
                url: '/story',
                templateUrl: "./views/story.html",
                controller: 'storyControl'
            })
        .state('levelDesc',
            {
                url: '/description',
                templateUrl: "./views/levelDesc.html",
                controller: 'levelDescControl'
            })
        .state('question',
            {
                url: '/question',
                templateUrl: "./views/question.html",
                controller: 'questionControl'
            })
        .state('info',
            {
                url: '/explanation',
                templateUrl: "./views/info.html",
                controller: 'infoControl'
            })
        .state('score',
            {
                url: '/score',
                templateUrl: "./views/score.html",
                controller: 'scoreControl'
            })
});