// very first load
setup();

var total_seconds = 0;
var STOP_TIMER = false;

function setup() {
    console.log("Init");
    // $.getJSON($SCRIPT_ROOT + '/get/time', {
        
    // }, function(data) {
    //     total_seconds = data.result;
    //     setTotalTime();
    // });
    auto_manual(true, false);
}

window.addEventListener('load', (e) => {
    
});

