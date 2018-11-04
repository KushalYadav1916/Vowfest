desktopNotification: function() {
    if (Notification.permission === "granted") {
      var text = "hello world";
      this.sendDesktopNotification(text);
    }
  },
sendDesktopNotification: function(text) {
    let notification = new Notification('Testing', {
      body: text,
      tag: 'Notification'
    }); 
notification.onclick = function() {
      parent.focus();
      this.close();
    };
    setTimeout(notification.close.bind(notification), 1000);
  }