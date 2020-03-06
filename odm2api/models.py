from __future__ import (absolute_import, division, print_function)

from odm2api.base import ModelBase

#def class_mapper:
#    for cls in ModelBase.__subclasses__:
#        cls = ModelBase.classes[cls.__name__]

#######################
### ODM2Annotations ###
#######################
class ActionAnnotations(ModelBase.classes.ActionAnnotations):
	pass
class CategoricalResultValueAnnotations(ModelBase.classes.CategoricalResultValueAnnotations):
	pass
class EquipmentAnnotations(ModelBase.classes.EquipmentAnnotations):
	pass
class MeasurementResultValueAnnotations(ModelBase.classes.MeasurementResultValueAnnotations):
	pass
class MethodAnnotations(ModelBase.classes.MethodAnnotations):
	pass
class PointCoverageResultValueAnnotations(ModelBase.classes.PointCoverageResultValueAnnotations):
	pass
class ProfileResultValueAnnotations(ModelBase.classes.ProfileResultValueAnnotations):
	pass
class ResultAnnotations(ModelBase.classes.ResultAnnotations):
	pass
class SamplingFeatureAnnotations(ModelBase.classes.SamplingFeatureAnnotations):
	pass
class SectionResultValueAnnotations(ModelBase.classes.SectionResultValueAnnotations):
	pass
class SpectraResultValueAnnotations(ModelBase.classes.SpectraResultValueAnnotations):
	pass
class TimeSeriesResultValueAnnotations(ModelBase.classes.TimeSeriesResultValueAnnotations):
	pass
class TrajectoryResultValueAnnotations(ModelBase.classes.TrajectoryResultValueAnnotations):
	pass
class TransectResultValueAnnotations(ModelBase.classes.TransectResultValueAnnotations):
	pass
class Annotations(ModelBase.classes.Annotations):
	pass

################
### ODM2Core ###
################
class ActionBy(ModelBase.classes.ActionBy):
	pass
class DatasetsResults(ModelBase.classes.DatasetsResults):
	pass
class RelatedActions(ModelBase.classes.RelatedActions):
	pass
class ProcessingLevels(ModelBase.classes.ProcessingLevels):
	pass
class Organizations(ModelBase.classes.Organizations):
	pass
class Variables(ModelBase.classes.Variables):
	pass
class FeatureActions(ModelBase.classes.FeatureActions):
	pass
class People(ModelBase.classes.People):
	pass
class Methods(ModelBase.classes.Methods):
	pass
class Datasets(ModelBase.classes.Datasets):
	pass
class Results(ModelBase.classes.Results):
	pass
class TaxonomicClassifiers(ModelBase.classes.TaxonomicClassifiers):
	pass
class SamplingFeatures(ModelBase.classes.SamplingFeatures):
	pass
class Affiliations(ModelBase.classes.Affiliations):
	pass
class Actions(ModelBase.classes.Actions):
	pass

################
### ODM2Core ###
################
class CV_LBNLICPMSMapper(ModelBase.classes.CV_LBNLICPMSMapper):
	pass
class CV_AnnotationType(ModelBase.classes.CV_AnnotationType):
	pass
class CV_ActionType(ModelBase.classes.CV_ActionType):
	pass
class CV_DatasetType(ModelBase.classes.CV_DatasetType):
	pass
class CV_MethodType(ModelBase.classes.CV_MethodType):
	pass
class CV_OrganizationType(ModelBase.classes.CV_OrganizationType):
	pass
class CV_ResultType(ModelBase.classes.CV_ResultType):
	pass
class CV_Status(ModelBase.classes.CV_Status):
	pass
class Units(ModelBase.classes.Units):
	pass
class CV_ElevationDatum(ModelBase.classes.CV_ElevationDatum):
	pass
class CV_SamplingFeatureGeoType(ModelBase.classes.CV_SamplingFeatureGeoType):
	pass
class CV_SamplingFeatureType(ModelBase.classes.CV_SamplingFeatureType):
	pass
class CV_TaxonomicClassifierDomain(ModelBase.classes.CV_TaxonomicClassifierDomain):
	pass
class CV_QuantityKind(ModelBase.classes.CV_QuantityKind):
	pass
class CV_VariableDomain(ModelBase.classes.CV_VariableDomain):
	pass
class CV_DataQualityType(ModelBase.classes.CV_DataQualityType):
	pass
class CV_EquipmentType(ModelBase.classes.CV_EquipmentType):
	pass
class CV_PropertyDataType(ModelBase.classes.CV_PropertyDataType):
	pass
class CV_DirectiveType(ModelBase.classes.CV_DirectiveType):
	pass
class CV_CensorCode(ModelBase.classes.CV_CensorCode):
	pass
class CV_QualityCode(ModelBase.classes.CV_QualityCode):
	pass
class CV_AggregationStatistic(ModelBase.classes.CV_AggregationStatistic):
	pass
class CV_FeaturesOfInterestType(ModelBase.classes.CV_FeaturesOfInterestType):
	pass
class CV_SpatialOffsetType(ModelBase.classes.CV_SpatialOffsetType):
	pass
class CV_Medium(ModelBase.classes.CV_Medium):
	pass
class CV_SpecimenType(ModelBase.classes.CV_SpecimenType):
	pass
class CV_RelationshipType(ModelBase.classes.CV_RelationshipType):
	pass

#######################
### ODM2DataQuality ###
#######################
class ReferenceMaterialValues(ModelBase.classes.ReferenceMaterialValues):
	pass
#PRT - TODO - This class doesn't auto map - need to come back to
#class ResultNormalizationValues(ModelBase.classes.ResultNormalizationValues):
#	pass
class DataQuality(ModelBase.classes.DataQuality):
	pass
class ResultsDataQuality(ModelBase.classes.ResultsDataQuality):
	pass
class ReferenceMaterials(ModelBase.classes.ReferenceMaterials):
	pass

#####################
### ODM2Equipment ###
#####################
class CalibrationReferenceEquipment(ModelBase.classes.CalibrationReferenceEquipment):
	pass
class CalibrationActions(ModelBase.classes.CalibrationActions):
	pass
class CalibrationStandards(ModelBase.classes.CalibrationStandards):
	pass
class DataLoggerFiles(ModelBase.classes.DataLoggerFiles):
	pass
class DataloggerFileColumns(ModelBase.classes.DataloggerFileColumns):
	pass
class DataloggerProgramFiles(ModelBase.classes.DataloggerProgramFiles):
	pass
class EquipmentUsed(ModelBase.classes.EquipmentUsed):
	pass
class EquipmentModels(ModelBase.classes.EquipmentModels):
	pass
class InstrumentOutputVariables(ModelBase.classes.InstrumentOutputVariables):
	pass
class MaintenanceActions(ModelBase.classes.MaintenanceActions):
	pass
class Equipment(ModelBase.classes.Equipment):
	pass
class RelatedEquipment(ModelBase.classes.RelatedEquipment):
	pass

###############################
### ODM2ExtensionProperties ###
###############################
class ActionExtensionPropertyValues(ModelBase.classes.ActionExtensionPropertyValues):
	pass
class CitationExtensionPropertyValues(ModelBase.classes.CitationExtensionPropertyValues):
	pass
class MethodExtensionPropertyValues(ModelBase.classes.MethodExtensionPropertyValues):
	pass
class ResultExtensionPropertyValues(ModelBase.classes.ResultExtensionPropertyValues):
	pass
class SamplingFeatureExtensionPropertyValues(ModelBase.classes.SamplingFeatureExtensionPropertyValues):
	pass
class ExtensionProperties(ModelBase.classes.ExtensionProperties):
	pass
class VariableExtensionPropertyValues(ModelBase.classes.VariableExtensionPropertyValues):
	pass

###############################
### ODM2ExternalIdentifiers ###
###############################
class CitationExternalIdentifiers(ModelBase.classes.CitationExternalIdentifiers):
	pass
class MethodExternalIdentifiers(ModelBase.classes.MethodExternalIdentifiers):
	pass
class PersonExternalIdentifiers(ModelBase.classes.PersonExternalIdentifiers):
	pass
class ReferenceMaterialExternalIdentifiers(ModelBase.classes.ReferenceMaterialExternalIdentifiers):
	pass
class SamplingFeatureExternalIdentifiers(ModelBase.classes.SamplingFeatureExternalIdentifiers):
	pass
class SpatialReferenceExternalIdentifiers(ModelBase.classes.SpatialReferenceExternalIdentifiers):
	pass
class TaxonomicClassifierExternalIdentifiers(ModelBase.classes.TaxonomicClassifierExternalIdentifiers):
	pass
class ExternalIdentifierSystems(ModelBase.classes.ExternalIdentifierSystems):
	pass
class VariableExternalIdentifiers(ModelBase.classes.VariableExternalIdentifiers):
	pass

#######################
### ODM2LabAnalyses ###
#######################
class ActionDirectives(ModelBase.classes.ActionDirectives):
	pass
class Directives(ModelBase.classes.Directives):
	pass
class SpecimenBatchPositions(ModelBase.classes.SpecimenBatchPositions):
	pass

######################
### ODM2Provenance ###
######################
class AuthorLists(ModelBase.classes.AuthorLists):
	pass
class DatasetCitations(ModelBase.classes.DatasetCitations):
	pass
class MethodCitations(ModelBase.classes.MethodCitations):
	pass
class RelatedAnnotations(ModelBase.classes.RelatedAnnotations):
	pass
class RelatedCitations(ModelBase.classes.RelatedCitations):
	pass
class RelatedDatasets(ModelBase.classes.RelatedDatasets):
	pass
class RelatedResults(ModelBase.classes.RelatedResults):
	pass
class DerivationEquations(ModelBase.classes.DerivationEquations):
	pass
#PRT TODO- this doesn't auto map, need to come back to
#class ResultDerivationEquations(ModelBase.classes.ResultDerivationEquations):
#	pass
class Citations(ModelBase.classes.Citations):
	pass

###################
### ODM2Results ###
###################
class CategoricalResultValues(ModelBase.classes.CategoricalResultValues):
	pass
class CategoricalResults(ModelBase.classes.CategoricalResults):
	pass
class MeasurementResultValues(ModelBase.classes.MeasurementResultValues):
	pass
class MeasurementResults(ModelBase.classes.MeasurementResults):
	pass
class PointCoverageResultValues(ModelBase.classes.PointCoverageResultValues):
	pass
class PointCoverageResults(ModelBase.classes.PointCoverageResults):
	pass
class ProfileResultValues(ModelBase.classes.ProfileResultValues):
	pass
class ProfileResults(ModelBase.classes.ProfileResults):
	pass
class SectionResultValues(ModelBase.classes.SectionResultValues):
	pass
class SectionResults(ModelBase.classes.SectionResults):
	pass
class SpectraResultValues(ModelBase.classes.SpectraResultValues):
	pass
class SpectraResults(ModelBase.classes.SpectraResults):
	pass
class TimeSeriesResultValues(ModelBase.classes.TimeSeriesResultValues):
	pass
class TimeSeriesResults(ModelBase.classes.TimeSeriesResults):
	pass
class TrajectoryResultValues(ModelBase.classes.TrajectoryResultValues):
	pass
class TrajectoryResults(ModelBase.classes.TrajectoryResults):
	pass
class TransectResultValues(ModelBase.classes.TransectResultValues):
	pass
class TransectResults(ModelBase.classes.TransectResults):
	pass

############################
### ODM2SamplingFeatures ###
############################
class SpatialReferences(ModelBase.classes.SpatialReferences):
	pass
class RelatedFeatures(ModelBase.classes.RelatedFeatures):
	pass
class FeaturesOfInterest(ModelBase.classes.FeaturesOfInterest):
	pass
class SampledFeatures(ModelBase.classes.SampledFeatures):
	pass
class SpatialOffsets(ModelBase.classes.SpatialOffsets):
	pass
class SpecimenTaxonomicClassifiers(ModelBase.classes.SpecimenTaxonomicClassifiers):
	pass
class Specimens(ModelBase.classes.Specimens):
	pass

######################
### ODM2Simulation ###
######################
class ModelAffiliations(ModelBase.classes.ModelAffiliations):
	pass
class RelatedModels(ModelBase.classes.RelatedModels):
	pass
class Models(ModelBase.classes.Models):
	pass
class Simulations(ModelBase.classes.Simulations):
	pass

