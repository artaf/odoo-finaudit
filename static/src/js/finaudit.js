odoo.define('finaudit.FormView', function (require) {
"use strict";

var core = require('web.core');
var QWeb = require('web.QWeb');
var session = require('web.session');
var utils = require('web.utils');
var FormView=require('web.FormView');

var qweb = core.qweb;

    FormView.include({
        init: function(parent, dataset, fields_view, options) {
            this._super(parent, dataset, fields_view, options);
            this.qweb = new QWeb(session.debug, {_s: session.origin});
            for (var i=0, ii=this.fields_view.arch.children.length; i < ii; i++) {
                var child = this.fields_view.arch.children[i];
                if (child.tag === "templates") {
//                    transform_qweb_template(child, this.fields_view, this.many2manys);
                    this.qweb.add_template(utils.json_node_to_xml(child));
                    break;
                }
            }
        },

/*        willStart: function() {
            this._super();
        },*/

/*        start: function() {
           this._super();
        },*/

        render: function () {
            var self = this;
//            var fragment = document.createDocumentFragment();
//            _.each(this.data.records, function (record) {
//                var kanban_record = new KanbanRecord(self, record, options);
//                self.widgets.push(kanban_record);
//                kanban_record.appendTo(fragment);
//            });
            var content;// = this.qweb.render('kanban-box', qweb_context);
//            this.$el.append(fragment);
            this.$el.append(content);
        },

    });

});
