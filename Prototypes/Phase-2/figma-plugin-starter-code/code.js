figma.showUI(__html__);

figma.ui.onmessage = (msg) => {
  if (msg.type === "draw") {
    const rect = figma.createRectangle();
    rect.resize(msg.width, msg.height);
    rect.x = 100;
    rect.y = 100;

    figma.currentPage.appendChild(rect);
  }
};