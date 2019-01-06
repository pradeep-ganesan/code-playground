'''Lottery picks selection'''

import argparse

class LotteryTicket(object):
    '''Lotter ticket selector'''
    def __init__(self, tickets=None):
        self.tickets = tickets or []
        self.codes_n = 7
        self.double_codes = 0

    def invalid_size(self, ticket):
        return len(ticket) > (self.codes_n * 2) or len(ticket) < self.codes_n

    def pick_my_tic(self):
        '''lotto picks'''
        picks = []

        def find_zero_substr(ticket):
            #ignoring leading zeroes
            start_0 = 2 if self.double_codes > 1 else len(ticket)
            while start_0 < (len(ticket) - 2):
                # ignoring trailing zeroes
                if ticket[start_0] not in '0' or ticket[start_0 + 1] not in '0':
                    start_0 += 1
                    continue
                else:
                    self.double_codes -= 2
                    break
            return start_0

        def valid_code(code, codes):
            code_val = int(code)
            if code_val >= 1 and code_val <= 59 and code not in codes:
                return True
            return False

        for ticket in self.tickets:
            codes = set()
            tic_len = len(ticket)

            if self.invalid_size(ticket):
                continue

            self.double_codes = tic_len - self.codes_n

            # special case where '00' is a substring of a ticket
            # first pass
            start_0 = find_zero_substr(ticket)
            start, end = -1, -1
            if start_0 < (tic_len - 2):
                start = start_0 - 1
                end = start_0 + 2
                code1 = ticket[start : (start + 2)]
                code2 = ticket[(end - 1) : (end + 1)]
                if not valid_code(code1, codes) or not valid_code(code2, codes):
                    print 'invalid codes'
                    continue
                else:
                    codes.add(code1)
                    codes.add(code2)

            i = 0
            while i < tic_len:
                #if start >= 0 and i >= start:
                #    i = end + 1
                    
                code_slice = ticket[i : i+2]
                code = int(code_slice)
                if code > 59 or not self.double_codes:
                    code_slice = ticket[i : i+1]
                    code = int(code_slice)
                    if not code:
                        break
                    i += 1
                elif code and self.double_codes:# and i < (start - 1):
                    i += 2
                    self.double_codes -= 1
                else:
                    break
                if code_slice not in codes:
                    codes.add(code_slice)
                else:
                    break
            if i < tic_len:
                continue
            picks.append(ticket)
            print codes
        return picks

def main():
    parser = argparse.ArgumentParser(
        description='Lottery ticket selector'
    )

    parser.add_argument(
        'ticketsfile',
        help='path to tickets file'
    )
    opts = parser.parse_args()

    def parsetickets(ticfile):
        '''get ticket list'''
        with open(ticfile, 'r') as ticfp:
            tickets = ticfp.read()
        return tickets.split(',')

    tickets = parsetickets(opts.ticketsfile)
    lottery = LotteryTicket(tickets)

    my_picks = lottery.pick_my_tic()
    print my_picks

if __name__ == '__main__':
    main()
