# Copyright 2016-2017 University of Helsinki.
#
# This file is part of data-driven-language-typology distribution.
#
# data-driven-language-typology is free software: you can
# redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# data-driven-language-typology is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with data-driven-language-typology.  If not, see
# <http://www.gnu.org/licenses/>.
#
from pimlico.core.modules.base import BaseModuleInfo
from pimlico.datatypes.results import NumericResult

from dlt.datatypes.ngram import UnigramFrequencyType, TokenMappingType


class ModuleInfo(BaseModuleInfo):
    module_type_name = "jaccard_index_distance"
    module_inputs = [("model_a", UnigramFrequencyType),
                     ("model_b", UnigramFrequencyType),
                     ("token_mapping", TokenMappingType)]
    module_outputs = [("distance", NumericResult)]
    module_options = {
        "min_frequency": {
            "help": "Minimum frequency in range [0, 1] for included tokens.",
            "required": False,
            "default": 0.00001,
            "type": float
        }
    }
