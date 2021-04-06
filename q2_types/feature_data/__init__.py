# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    TaxonomyFormat, TaxonomyDirectoryFormat, HeaderlessTSVTaxonomyFormat,
    HeaderlessTSVTaxonomyDirectoryFormat, TSVTaxonomyFormat,
    TSVTaxonomyDirectoryFormat, DNAFASTAFormat, DNASequencesDirectoryFormat,
    PairedDNASequencesDirectoryFormat, AlignedDNAFASTAFormat,
    AlignedDNASequencesDirectoryFormat, DifferentialFormat,
    DifferentialDirectoryFormat, FASTAFormat, AlignedFASTAFormatMixin,
    AlignedProteinSequencesDirectoryFormat, ProteinSequencesDirectoryFormat,
    ProteinFASTAFormat, AlignedProteinFASTAFormat, RNASequencesDirectoryFormat,
    RNAFASTAFormat, AlignedRNAFASTAFormat, AlignedRNASequencesDirectoryFormat,
    PairedRNASequencesDirectoryFormat, NucleicAcidFASTAFormat,
    AlignedNucleicAcidFASTAFormat, AlignedNucleicAcidSequencesDirectoryFormat,
    NucleicAcidSequencesDirectoryFormat, AlignedGenericFASTAFormat,
    GenericFASTAFormat, GenericSequencesDirectoryFormat,
    AlignedGenericSequencesDirectoryFormat)
from ._type import (
    FeatureData, Taxonomy, Sequence, PairedEndSequence, AlignedSequence,
    Differential, ProteinSequence, AlignedProteinSequence, RNASequence,
    AlignedRNASequence, PairedEndRNASequence)

# TODO remove these imports when tests are rewritten. Remove from __all__ too
from ._transformer import (
    NucleicAcidIterator, AlignedNucleicAcidIterator, DNAIterator,
    PairedDNAIterator, AlignedDNAIterator, ProteinIterator,
    AlignedProteinIterator, RNAIterator, AlignedRNAIterator, PairedRNAIterator,
    GenericSequenceIterator, AlignedGenericSequenceIterator)

__all__ = [
    'TaxonomyFormat', 'TaxonomyDirectoryFormat', 'HeaderlessTSVTaxonomyFormat',
    'HeaderlessTSVTaxonomyDirectoryFormat', 'TSVTaxonomyFormat',
    'TSVTaxonomyDirectoryFormat', 'DNAFASTAFormat', 'DifferentialFormat',
    'DNASequencesDirectoryFormat', 'PairedDNASequencesDirectoryFormat',
    'AlignedDNAFASTAFormat', 'AlignedDNASequencesDirectoryFormat',
    'FeatureData', 'Taxonomy', 'Sequence', 'PairedEndSequence',
    'AlignedSequence', 'NucleicAcidIterator', 'DNAIterator',
    'PairedDNAIterator', 'FASTAFormat', 'AlignedDNAIterator', 'Differential',
    'DifferentialDirectoryFormat', 'AlignedFASTAFormatMixin',
    'ProteinFASTAFormat', 'ProteinSequence', 'AlignedProteinFASTAFormat',
    'ProteinSequencesDirectoryFormat', 'AlignedProteinSequence',
    'AlignedProteinSequencesDirectoryFormat', 'ProteinIterator',
    'AlignedProteinIterator', 'RNAIterator', 'AlignedRNAIterator',
    'RNAFASTAFormat', 'AlignedRNAFASTAFormat', 'RNASequencesDirectoryFormat',
    'AlignedRNASequencesDirectoryFormat', 'RNASequence', 'AlignedRNASequence',
    'PairedRNAIterator', 'PairedRNASequencesDirectoryFormat',
    'PairedEndRNASequence', 'GenericSequenceIterator',
    'AlignedGenericSequenceIterator', 'NucleicAcidFASTAFormat',
    'AlignedNucleicAcidFASTAFormat', 'AlignedNucleicAcidIterator'
    'AlignedNucleicAcidSequencesDirectoryFormat',
    'NucleicAcidSequencesDirectoryFormat', 'AlignedGenericFASTAFormat',
    'GenericFASTAFormat', 'GenericSequencesDirectoryFormat',
    'AlignedGenericSequencesDirectoryFormat']

importlib.import_module('q2_types.feature_data._transformer')
