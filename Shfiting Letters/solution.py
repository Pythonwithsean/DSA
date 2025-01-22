from typing import List
import heapq

class Solution:
    def rotate_letter(self, c: str, n: int) -> str:
		# Calculate new position of letter c after n rotations.
        new_pos = (ord(c) - ord('a') + n) % 26
        return chr(ord('a') + new_pos)

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        numchars = len(s)
        num_shifts = len(shifts)

        # Sort the shifts so that we can apply them sequentially to
        # the input string.
        shifts.sort(key = lambda l : l[0])

        # Work through the sorted shifts in order of the start position.
        next_shift_to_add = 0
        # charpos is the next character to apply a shift to.
        charpos, next_end, direction = shifts[next_shift_to_add]
        # Keep track of the cumulative rotations to be applied to
        # the next character.
        rotations = 1 if direction == 1 else -1

        # Keep an ordered list of the end points of the currently
        # active shifts, so as to be able to detect when a shift
        # no longer applies.
        # The heap stores tuples: (end-of-shift, rotation (-1 or +1))
        heap = []
        heapq.heappush(heap, (next_end, rotations))

        result = ''
        # Start building the result from any characters at the start
        # that have no rotation applied to them.
        for i in range(0, charpos):
            result += s[i]

        # Which will be the next shift to apply once charpos matches
        # its start position.
        next_shift_to_add += 1

        finished = False
        while not finished:
            # Add in further shifts with the same starting point as charpos.
            while next_shift_to_add < num_shifts and shifts[next_shift_to_add][0] == charpos:
                start, end, direction = shifts[next_shift_to_add]
                adjustment = 1 if direction == 1 else -1
                rotations += adjustment
                heapq.heappush(heap, (end, adjustment))
                next_shift_to_add += 1
                # The added shift could have an earlier stopping point
                # than previous ones.
                next_end = heap[0][0]

            # Apply the current rotation to the current letter of s.
            result += self.rotate_letter(s[charpos], rotations)
            # Move on to the next letter.
            charpos += 1
            if charpos > next_end:
                # Discontinue one of the currently active shifts.
                # There could be more than one that stops at this point.
                while heap and heap[0][0] == next_end:
                    _, adjustment = heapq.heappop(heap)
                    # Remove the rotation it contributed.
                    rotations -= adjustment

                if charpos < numchars:
                    # If there are still active shifts, find the earliest
                    # stopping point.
                    if heap:
                        next_end = heap[0][0]
                    elif next_shift_to_add < num_shifts:
                        # None currently active.
                        assert rotations == 0
                        # Append a section of the original that has no
                        # rotations applied to it.
                        result += s[charpos:shifts[next_shift_to_add][0]]
                        # Skip ahead to where the next rotation applies.
                        charpos = shifts[next_shift_to_add][0]
                    else:
                        # No more shifts to be applied.
                        finished = True
                else:
                    # End of the input reached.
                    finished = True
        result += s[charpos:]
        return result

soln = Solution()
s = 'abc'
shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(soln.shiftingLetters(s,shifts))
assert soln.shiftingLetters(s, shifts) == 'ace'