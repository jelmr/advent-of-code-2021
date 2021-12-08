from solutions.solution08 import Solution08


class Solution08B(Solution08):

    @staticmethod
    def is_subsegment(a, b):
        return set(a) & set(b) == set(a)

    def solve(self, input_text):
        final_result = 0
        for line in input_text:
            signals, outputs = line.split(' | ')
            signals = signals.split(' ')
            outputs = outputs.split(' ')

            known_signals = dict()
            for signal in signals:
                match len(signal):
                    case 2:
                        known_signals[1] = signal
                    case 3:
                        known_signals[7] = signal
                    case 4:
                        known_signals[4] = signal
                    case 7:
                        known_signals[8] = signal

            for signal in signals:
                match len(signal):
                    case 5:
                        if self.is_subsegment(known_signals[1], signal):
                            known_signals[3] = signal
                        else:
                            if len(set(signal) | set(known_signals[4])) == 6:
                                known_signals[5] = signal
                            else:
                                known_signals[2] = signal

                    case 6:
                        if self.is_subsegment(known_signals[1], signal):
                            if self.is_subsegment(known_signals[4], signal):
                                known_signals[9] = signal
                            else:
                                known_signals[0] = signal
                        else:
                            known_signals[6] = signal

            reverse_signal_mapping = dict()
            for k, v in known_signals.items():
                reverse_signal_mapping[''.join(sorted(v))] = k

            result = ''
            for x in outputs:
                result += str(reverse_signal_mapping[''.join(sorted(x))])

            final_result += int(result)

        return final_result