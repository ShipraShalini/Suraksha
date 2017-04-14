/**
 * Created by moonlace on 14/04/17.
 */
var suraksha = angular.module('suraksha', [
    'ui.router'
]);

suraksha.run(function ($rootScope) {
    console.log('App initialise');
});

suraksha.config(function ($stateProvider) {
    $stateProvider
        .state('info',
            {
                url: '/',
                templateUrl: "./views/info.html",
                controller: 'infoControl'
            })
        .state('question',
            {
                url: '/question',
                templateUrl: "./views/question.html",
                controller: "questionControl"
            })
    .state('storyLine',
            {
                url: '/storyLine',
                templateUrl: "./views/storyline.html",
                controller: "storyLineControl"
            })

});