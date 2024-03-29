(function () {
    'use strict';

    angular
        .module('app.lazarus',
            [
                // 3rd Party Dependencies
                'flow'
            ]
        )
        .config(config);

    /** @ngInject */
    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        // State
        $stateProvider.state('app.lazarus', {
            url: '/lazarus',
            views: {
                'content@app': {
                    templateUrl: '/static/app/main/apps/lazarus/lazarus.html',
                    controller: 'LazarusController as vm'
                }
            },
            bodyClass: 'file-manager'
        });
        
        // msNavigationServiceProvider.saveItem('apps.lazarus', {
        //     title: 'Lazarus',
        //     icon: 'icon-folder',
        //     state: 'app.lazarus',
        //     weight: 5
        // });
    
    
    
    
    
    
    
    
    
    }})();
