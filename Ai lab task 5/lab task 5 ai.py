leaf_counter = 0

def minimax(node, depth, is_maximizing):
    global leaf_counter
    if is_terminal(node):
        leaf_counter += 1
        return get_value(node)
    
    if is_maximizing:
        max_eval = -infinity
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = infinity
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval