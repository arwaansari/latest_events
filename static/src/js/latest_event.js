odoo.define('latest_events.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
       console.log('ssssss')
           var self = this;
           rpc.query({
               route: '/latest_events',
               params: {},
           }).then(function (result) {
            var name = result;
            $('.qweb_event').append(Qweb.render('latest_events.event_template', {name}));
//           var event_id = Object.values(result)
//           var event_name = Object.keys(result)
//           console.log(result)
//               self.$('#event_name').text(event_name);
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});