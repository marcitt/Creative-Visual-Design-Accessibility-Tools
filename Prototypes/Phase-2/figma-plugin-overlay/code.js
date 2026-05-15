/*global figma, __html__*/
/*jslint asyncs*/
// what is this actually doing besides fixing the jslint errors?

figma.showUI(__html__, { width: 200, height: 100 });

function sendStatus(text) {
    figma.ui.postMessage({ type: "status", text });
}

async function sendData() {
    const nodes = figma.currentPage.findAll((n) => n.visible);

    const payload = {
        nodes: nodes.map(function(n) {
            const bbox = n.absoluteBoundingBox || { x: 0, y: 0, width: 0,
                 height: 0 };
            return {
                id: n.id,
                name: n.name,
                type: n.type,
                x: bbox.x,
                y: bbox.y,
                width: bbox.width,
                height: bbox.height
            };
        }),
        viewport: {
            x: figma.viewport.bounds.x,
            y: figma.viewport.bounds.y,
            zoom: figma.viewport.zoom
        }
    };

    try {
        await fetch("http://localhost:8000/update", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        console.log("hello");
        sendStatus("success");
    } catch (e) {
        sendStatus("failure");
    }
}

setInterval(sendData, 1000);
