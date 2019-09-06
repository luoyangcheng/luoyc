
$.ajax({
    url: "192.168.3.188:6088",
    data: {"id": id}, //以键/值对的形式
    async: false,
    dataType: "json",
    success: function (data) {
        alert("firstName = " + data.firstName);
    }
});