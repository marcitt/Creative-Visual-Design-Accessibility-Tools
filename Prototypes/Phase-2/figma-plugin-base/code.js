figma.showUI(__html__, { width: 400, height: 200 });

// messages have this structure:
// {{"type": "select", "query": "Layer Name"}}

figma.ui.onmessage = async (msg) => {
  await handleCommand(msg);
};

async function handleCommand(msg) {
    console.log(msg);
    if (msg.type === "select") {

        const objects = msg.query;

        const nodes = objects
            .map(q => figma.currentPage.findOne(n => n.name === q))
            .filter(Boolean)

        figma.currentPage.selection = nodes
    }

    // zoom onto single object
    if (msg.type === "object zoom") {
        const node = figma.currentPage.findOne(n => n.name === msg.query)

        if (node) {
            figma.viewport.scrollAndZoomIntoView([node]);
        }
    }

    // zoom
    if (msg.type === "zoom") {
        figma.viewport.zoom = msg.query;
    }

    // pan
    if (msg.type === "pan") {
        const coords = msg.query;
        const x_pan = coords["x"];
        const y_pan = coords["y"];

        //  get current viewport centre
        const center = figma.viewport.center;

        figma.viewport.center = {
            x: center.x + x_pan,
            y: center.y + y_pan
        };

    }

    // centre object
    if (msg.type === "object pan") {
        const node = figma.currentPage.findOne(n => n.name === msg.query)

        if (node && node.absoluteBoundingBox) {
            // Scroll so node is centered
            figma.viewport.center = {
                x: node.absoluteBoundingBox.x + node.absoluteBoundingBox.width / 2,
                y: node.absoluteBoundingBox.y + node.absoluteBoundingBox.height / 2
            };
        };
    }
}

