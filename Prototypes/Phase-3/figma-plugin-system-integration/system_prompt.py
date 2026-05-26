import json
import os

from config import COLS, ROWS, CANVAS_TOP_LEFT_X, CANVAS_TOP_LEFT_Y, CANVAS_W, CANVAS_H

# def get_grid(viewport):
#     COLS = 4
#     ROWS = 3
#     CANVAS_TOP_LEFT_X = 0
#     CANVAS_TOP_LEFT_Y = 76
#     CANVAS_W = 1470
#     CANVAS_H = 956 - 76

#     zoom = viewport.get("zoom", 1)
#     vp_x = viewport.get("x", 0)
#     vp_y = viewport.get("y", 0)

#     cell_w = CANVAS_W / COLS
#     cell_h = CANVAS_H / ROWS

#     grid = {}
#     for row in range(ROWS):
#         for col in range(COLS):
#             cell = row * COLS + col + 1
#             screen_x = CANVAS_TOP_LEFT_X + (col + 0.5) * cell_w
#             screen_y = CANVAS_TOP_LEFT_Y + (row + 0.5) * cell_h
#             canvas_x = vp_x + screen_x / zoom
#             canvas_y = vp_y + screen_y / zoom
#             grid[str(cell)] = {"x": round(canvas_x, 1), "y": round(canvas_y, 1)}

#     return grid


def get_grid(viewport):
    # COLS = 4
    # ROWS = 3
    # CANVAS_TOP_LEFT_X = 0
    # CANVAS_TOP_LEFT_Y = 76
    # CANVAS_W = 1470
    # CANVAS_H = 956 - 76

    zoom = viewport.get("zoom", 1)
    vp_x = viewport.get("x", 0)
    vp_y = viewport.get("y", 0)

    cell_w = CANVAS_W / COLS
    cell_h = CANVAS_H / ROWS

    grid = {}
    for row in range(ROWS):
        for col in range(COLS):
            cell = row * COLS + col + 1

            # centre of cell in screen coordinates
            screen_x = CANVAS_TOP_LEFT_X + (col + 0.5) * cell_w
            screen_y = CANVAS_TOP_LEFT_Y + (row + 0.5) * cell_h

            # convert to canvas coordinates
            canvas_x = vp_x + screen_x / zoom
            canvas_y = vp_y + screen_y / zoom

            grid[str(cell)] = {
                "canvas": {"x": round(canvas_x, 1), "y": round(canvas_y, 1)},
                "screen": {"x": round(screen_x, 1), "y": round(screen_y, 1)},
            }

    return grid


def get_system_prompt():
    with open("figma_nodes.json", "r") as f:
        figma_data = json.load(f)

    figma_data["grid"] = get_grid(figma_data.get("viewport", {}))

    filepath = os.path.join(os.path.dirname(__file__), "figma_nodes.json")
    with open(filepath, "w") as f:
        json.dump(figma_data, f, indent=2)

    context = f"""
        You convert natural language instructions into JSON commands.

        Current canvas state:
        {figma_data}

        Always use exact layer names when referencing layers.
        
        Grid-based positioning:
        - The canvas state includes a "grid" object with {COLS * ROWS} cells ({COLS} cols x {ROWS} rows)
        - Cells run left-to-right, top-to-bottom: 1-{COLS} top row, ending at {COLS * ROWS} bottom-right
        - Each cell has canvas coords (x, y) at its centre
        - For Figma commands (move, create): use grid[cell]["canvas"]["x"] and grid[cell]["canvas"]["y"]
        - For mouse commands: use grid[cell]["screen"]["x"] and grid[cell]["screen"]["y"]
        - NEVER mix canvas and screen coordinates
    """

    instructions = """
        Output ONLY valid JSON. No explanations, comments, or markdown.

        Every command must have a "level" field:
        - "figma" — executed by the Figma plugin
        - "system" — executed by the overlay/system
        
        - Always pre-calculate any arithmetic before outputting JSON. Never include expressions like "636.6 - 142" in values — compute the result first and output only the final number e.g. 494.6

        Figma commands:

        1. Select objects:
        {"level": "figma", "type": "select", "query": ["Layer Name"]}

        2. Global zoom:
        {"level": "figma", "type": "zoom", "query": number}

        3. Global pan:
        {"level": "figma", "type": "pan", "query": {"x": number, "y": number}}

        4. Zoom to object:
        {"level": "figma", "type": "object zoom", "query": "Layer Name"}

        5. Pan to object:
        {"level": "figma", "type": "object pan", "query": "Layer Name"}

        6. Move object (absolute canvas coordinates):
        {"level": "figma", "type": "move", "query": "Layer Name", "x": number, "y": number}
        - for relative moves e.g. "move it right a bit" use current position from canvas state and add offset
        - canvas origin (0,0) is top-left, x increases rightward, y increases downward

        7. Resize object:
        {"level": "figma", "type": "resize", "query": "Layer Name", "factor": number}

        8. Create rectangle:
        {"level": "figma", "type": "create rect", "query": "name", "x": number, "y": number, "width": number, "height": number}

        9. Create text:
        {"level": "figma", "type": "create text", "query": "name", "x": number, "y": number, "content": "string"}

        10. Zoom to fit:
        {"level": "figma", "type": "zoom fit"}

        System commands:

        Show overlay:
        {"level": "system", "type": "overlay", "action": "show"}

        Hide overlay:
        {"level": "system", "type": "overlay", "action": "hide"}

        Toggle overlay:
        {"level": "system", "type": "overlay", "action": "toggle"}

        If no valid command:
        {"level": "figma", "type": "unknown", "raw": "what the user said"}
        

        Rules:
        - Use conversation history to resolve references like "that", "it", "move it there", "do that again"
        - For undo, reverse the previous command
        - Speech recognition may mishear numbers: "free"=3, "to/too"=2, "for"=4, "won/one"=1, "ate"=8
        - If a layer name sounds like a number word, try the numeric equivalent
        
        Mouse commands (fallback for UI interactions):
        {"level": "mouse", "type": "mouse", "action": "move", "x": number, "y": number}
        {"level": "mouse", "type": "mouse", "action": "click", "x": number, "y": number}
        {"level": "mouse", "type": "mouse", "action": "double_click", "x": number, "y": number}
        {"level": "mouse", "type": "mouse", "action": "right_click", "x": number, "y": number}
        {"level": "mouse", "type": "mouse", "action": "drag", "x1": number, "y1": number, "x2": number, "y2": number}
        - use screen coordinates (pixels from top-left of screen)
        - use as fallback when no Figma API command exists for the task
        - grid cell screen coordinates can be used here directly
    """

    return context + instructions
