### BUGS

- right_paren_idx isn't correct for nested parens
- when the recursion for the match plus doesn't find a match on either side it'll go back up the stack and call match_pattern for all of the previously matched chars, this is leading to the groups being popped incorrectly, need to figure out how to handle the match plus correctly
