/**
 * Created by wuyongxing on 15-2-12.
 */
$(function () {
    $($('#tabId').val()).addClass('active')
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}