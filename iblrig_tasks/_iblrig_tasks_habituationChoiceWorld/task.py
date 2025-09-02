from pathlib import Path
import yaml

import iblrig.misc
from iblrig.base_choice_world import HabituationChoiceWorldSession

# read defaults from task_parameters.yaml
with open(Path(__file__).parent.joinpath('task_parameters.yaml')) as f:
    DEFAULTS = yaml.safe_load(f)

class Session(HabituationChoiceWorldSession):
    @staticmethod
    def extra_parser():
        """:return: argparse.parser()"""
        parser = super(Session, Session).extra_parser()
        parser.add_argument(
            '--contrast_set',
            option_strings=['--contrast_set'],
            dest='contrast_set',
            default=DEFAULTS['CONTRAST_SET'],
            nargs='+',
            type=float,
            help='Set of contrasts to present',
        )
        parser.add_argument(
            '--reward_amount_ul',
            option_strings=['--reward_amount_ul'],
            dest='reward_amount_ul',
            default=DEFAULTS['REWARD_AMOUNT_UL'],
            type=float,
            help='reward amount',
        )
        parser.add_argument(
            '--delay_to_stim_center',
            option_strings=['--delay_to_stim_center'],
            dest='delay_to_stim_center',
            default=DEFAULTS['DELAY_TO_STIM_CENTER'],
            type=float,
            help='mean time to stimulus centering (s)',
        )
        parser.add_argument(
            '--randomize_delay',
            option_strings=['--randomize_delay'],
            dest='randomize_delay',
            default=DEFAULTS['RANDOMIZE_DELAY'],
            type=bool,
            help='indroduce random delay before stimulus centering',
        )
        parser.add_argument(
            '--iti_delay_secs',
            option_strings=['--iti_delay_secs'],
            dest='iti_delay_secs',
            default=DEFAULTS['ITI_DELAY_SECS'],
            type=float,
            help='',
        )
        parser.add_argument(
            '--iti_secs',
            option_strings=['--dead_time'],
            dest='dead_time',
            default=DEFAULTS['ITI_SECS'],
            type=float,
            help='',
        )
        parser.add_argument(
            '--stim_center_time_secs',
            option_strings=['--stim_center_time_secs'],
            dest='stim_center_time_secs',
            default=DEFAULTS['STIM_CENTER_TIME_SECS'],
            type=float,
            help='',
        )
        return parser


if __name__ == '__main__':  # pragma: no cover
    kwargs = iblrig.misc.get_task_arguments(parents=[Session.extra_parser()])
    sess = Session(**kwargs)
    sess.run()
