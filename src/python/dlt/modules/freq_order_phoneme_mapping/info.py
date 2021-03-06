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

from dlt.datatypes.ngram import TokenMappingType, UnigramFrequencyType, BigramModelType, TrigramModelType
from langsim.datatypes.raw_lines import RawTextLinesDocumentType
from pimlico.core.modules.base import BaseModuleInfo
from pimlico.datatypes.base import MultipleInputs
from pimlico.datatypes.tar import TarredCorpusType


class ModuleInfo(BaseModuleInfo):
    module_type_name = "token_mapping"
    module_inputs = [("unigram_models", MultipleInputs(UnigramFrequencyType)),
                     ("bigram_models", MultipleInputs(BigramModelType)),
                     ("trigram_models", MultipleInputs(TrigramModelType)),
                     ("corpora", MultipleInputs(TarredCorpusType(RawTextLinesDocumentType)))]
    module_outputs = [("mappings", TokenMappingType)]
    module_options = {
        "count": {
            "help": "How many tokens to process",
            "required": True,
            "type": int,
        },
        "phoneme_similarity_mapping_path": {
            "help": "Path to the ipa.bitdist.table file (incl. filename).",
            "required": True,
            "type": str,
        }
    }
