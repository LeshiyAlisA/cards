Ext.onReady(function(){
    Ext.create('Ext.form.Panel', {
        renderTo: Ext.getBody(),
        frame:true,
        title: 'User Form',
        height: 230,
        width: 280,
        bodyPadding: 10,
        defaultType: 'textfield',
        items: [
            {
                fieldLabel: 'First Name',
                name: 'firstName'
            },
            {
                fieldLabel: 'Last Name',
                name: 'lastName'
            },
            {
                xtype     : 'textareafield',
                grow      : true,
                name      : 'message',
                fieldLabel: 'Message',
                anchor    : '100%'
            }
        ],
        buttons: [{
            text: 'Save',
            formBind: true,
            handler: function(){
                this.up('form').getForm().submit({
                    url: '/list/',
                    submitEmptyText: false,
                    method: 'GET',
                    waitMsg: 'Saving Data...'
                });
            }
        },{
            text: 'Cancel'
        }]
    });
    simple.render(document.body);

});