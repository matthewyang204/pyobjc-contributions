# This file is generated by objective.metadata
#
# Last update: Sat May 11 10:54:37 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$MLCActivationTypeAbsolute@6$MLCActivationTypeCELU@13$MLCActivationTypeClamp@20$MLCActivationTypeELU@9$MLCActivationTypeGELU@18$MLCActivationTypeHardShrink@14$MLCActivationTypeHardSigmoid@4$MLCActivationTypeHardSwish@19$MLCActivationTypeLinear@2$MLCActivationTypeLogSigmoid@11$MLCActivationTypeNone@0$MLCActivationTypeReLU@1$MLCActivationTypeReLUN@10$MLCActivationTypeSELU@12$MLCActivationTypeSigmoid@3$MLCActivationTypeSoftPlus@7$MLCActivationTypeSoftShrink@15$MLCActivationTypeSoftSign@8$MLCActivationTypeTanh@5$MLCActivationTypeTanhShrink@16$MLCActivationTypeThreshold@17$MLCArithmeticOperationAcos@13$MLCArithmeticOperationAcosh@19$MLCArithmeticOperationAdd@0$MLCArithmeticOperationAsin@12$MLCArithmeticOperationAsinh@18$MLCArithmeticOperationAtan@14$MLCArithmeticOperationAtanh@20$MLCArithmeticOperationCeil@6$MLCArithmeticOperationCos@10$MLCArithmeticOperationCosh@16$MLCArithmeticOperationDivide@3$MLCArithmeticOperationDivideNoNaN@27$MLCArithmeticOperationExp@22$MLCArithmeticOperationExp2@23$MLCArithmeticOperationFloor@4$MLCArithmeticOperationLog@24$MLCArithmeticOperationLog2@25$MLCArithmeticOperationMax@29$MLCArithmeticOperationMin@28$MLCArithmeticOperationMultiply@2$MLCArithmeticOperationMultiplyNoNaN@26$MLCArithmeticOperationPow@21$MLCArithmeticOperationRound@5$MLCArithmeticOperationRsqrt@8$MLCArithmeticOperationSin@9$MLCArithmeticOperationSinh@15$MLCArithmeticOperationSqrt@7$MLCArithmeticOperationSubtract@1$MLCArithmeticOperationTan@11$MLCArithmeticOperationTanh@17$MLCComparisonOperationEqual@0$MLCComparisonOperationGreater@3$MLCComparisonOperationGreaterOrEqual@5$MLCComparisonOperationLess@2$MLCComparisonOperationLessOrEqual@4$MLCComparisonOperationLogicalAND@6$MLCComparisonOperationLogicalNAND@9$MLCComparisonOperationLogicalNOR@10$MLCComparisonOperationLogicalNOT@8$MLCComparisonOperationLogicalOR@7$MLCComparisonOperationLogicalXOR@11$MLCComparisonOperationNotEqual@1$MLCConvolutionTypeDepthwise@2$MLCConvolutionTypeStandard@0$MLCConvolutionTypeTransposed@1$MLCDataTypeBoolean@4$MLCDataTypeFloat16@3$MLCDataTypeFloat32@1$MLCDataTypeInt32@7$MLCDataTypeInt64@5$MLCDataTypeInt8@8$MLCDataTypeInvalid@0$MLCDataTypeUInt8@9$MLCDeviceTypeANE@3$MLCDeviceTypeAny@2$MLCDeviceTypeCPU@0$MLCDeviceTypeGPU@1$MLCExecutionOptionsForwardForInference@8$MLCExecutionOptionsForwardOnlyForInference@8$MLCExecutionOptionsNone@0$MLCExecutionOptionsPerLayerProfiling@16$MLCExecutionOptionsProfiling@4$MLCExecutionOptionsSkipWritingInputDataToDevice@1$MLCExecutionOptionsSynchronous@2$MLCGradientClippingTypeByGlobalNorm@2$MLCGradientClippingTypeByNorm@1$MLCGradientClippingTypeByValue@0$MLCGraphCompilationOptionsComputeAllGradients@8$MLCGraphCompilationOptionsDebugLayers@1$MLCGraphCompilationOptionsDisableLayerFusion@2$MLCGraphCompilationOptionsLinkGraphs@4$MLCGraphCompilationOptionsNone@0$MLCLSTMResultModeOutput@0$MLCLSTMResultModeOutputAndStates@1$MLCLossTypeCategoricalCrossEntropy@4$MLCLossTypeCosineDistance@7$MLCLossTypeHinge@5$MLCLossTypeHuber@6$MLCLossTypeLog@8$MLCLossTypeMeanAbsoluteError@0$MLCLossTypeMeanSquaredError@1$MLCLossTypeSigmoidCrossEntropy@3$MLCLossTypeSoftmaxCrossEntropy@2$MLCPaddingPolicySame@0$MLCPaddingPolicyUsePaddingSize@2$MLCPaddingPolicyValid@1$MLCPaddingTypeConstant@3$MLCPaddingTypeReflect@1$MLCPaddingTypeSymmetric@2$MLCPaddingTypeZero@0$MLCPoolingTypeAverage@2$MLCPoolingTypeL2Norm@3$MLCPoolingTypeMax@1$MLCRandomInitializerTypeGlorotUniform@2$MLCRandomInitializerTypeInvalid@0$MLCRandomInitializerTypeUniform@1$MLCRandomInitializerTypeXavier@3$MLCReductionTypeAll@9$MLCReductionTypeAny@8$MLCReductionTypeArgMax@5$MLCReductionTypeArgMin@6$MLCReductionTypeL1Norm@7$MLCReductionTypeMax@3$MLCReductionTypeMean@2$MLCReductionTypeMin@4$MLCReductionTypeNone@0$MLCReductionTypeSum@1$MLCRegularizationTypeL1@1$MLCRegularizationTypeL2@2$MLCRegularizationTypeNone@0$MLCSampleModeLinear@1$MLCSampleModeNearest@0$MLCSoftmaxOperationLogSoftmax@1$MLCSoftmaxOperationSoftmax@0$"""
misc.update(
    {
        "MLCSampleMode": NewType("MLCSampleMode", int),
        "MLCArithmeticOperation": NewType("MLCArithmeticOperation", int),
        "MLCExecutionOptions": NewType("MLCExecutionOptions", int),
        "MLCReductionType": NewType("MLCReductionType", int),
        "MLCComparisonOperation": NewType("MLCComparisonOperation", int),
        "MLCGradientClippingType": NewType("MLCGradientClippingType", int),
        "MLCRegularizationType": NewType("MLCRegularizationType", int),
        "MLCDeviceType": NewType("MLCDeviceType", int),
        "MLCLossType": NewType("MLCLossType", int),
        "MLCPoolingType": NewType("MLCPoolingType", int),
        "MLCConvolutionType": NewType("MLCConvolutionType", int),
        "MLCPaddingPolicy": NewType("MLCPaddingPolicy", int),
        "MLCRandomInitializerType": NewType("MLCRandomInitializerType", int),
        "MLCLSTMResultMode": NewType("MLCLSTMResultMode", int),
        "MLCDataType": NewType("MLCDataType", int),
        "MLCActivationType": NewType("MLCActivationType", int),
        "MLCSoftmaxOperation": NewType("MLCSoftmaxOperation", int),
        "MLCPaddingType": NewType("MLCPaddingType", int),
        "MLCGraphCompilationOptions": NewType("MLCGraphCompilationOptions", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "MLCPaddingTypeDebugDescription": (b"@i",),
    "MLCReductionTypeDebugDescription": (b"@i",),
    "MLCLossTypeDebugDescription": (b"@i",),
    "MLCGradientClippingTypeDebugDescription": (b"@i",),
    "MLCComparisonOperationDebugDescription": (b"@i",),
    "MLCLSTMResultModeDebugDescription": (b"@Q",),
    "MLCPoolingTypeDebugDescription": (b"@i",),
    "MLCActivationTypeDebugDescription": (b"@i",),
    "MLCPaddingPolicyDebugDescription": (b"@i",),
    "MLCConvolutionTypeDebugDescription": (b"@i",),
    "MLCSoftmaxOperationDebugDescription": (b"@i",),
    "MLCArithmeticOperationDebugDescription": (b"@i",),
    "MLCSampleModeDebugDescription": (b"@i",),
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MLCAdamOptimizer",
        b"optimizerWithDescriptor:beta1:beta2:epsilon:usesAMSGrad:timeStep:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(b"MLCAdamOptimizer", b"usesAMSGrad", {"retval": {"type": b"Z"}})
    r(
        b"MLCAdamWOptimizer",
        b"optimizerWithDescriptor:beta1:beta2:epsilon:usesAMSGrad:timeStep:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(b"MLCAdamWOptimizer", b"usesAMSGrad", {"retval": {"type": b"Z"}})
    r(
        b"MLCConvolutionDescriptor",
        b"isConvolutionTranspose",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MLCConvolutionDescriptor",
        b"usesDepthwiseConvolution",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MLCDevice",
        b"deviceWithType:selectsMultipleComputeDevices:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"MLCEmbeddingDescriptor",
        b"descriptorWithEmbeddingCount:embeddingDimension:paddingIndex:maximumNorm:pNorm:scalesGradientByFrequency:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"MLCEmbeddingDescriptor",
        b"scalesGradientByFrequency",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MLCGraph",
        b"bindAndWriteData:forInputs:toDevice:batchSize:synchronous:",
        {"retval": {"type": b"Z"}, "arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MLCGraph",
        b"bindAndWriteData:forInputs:toDevice:synchronous:",
        {"retval": {"type": "Z"}, "arguments": {5: {"type": "Z"}}},
    )
    r(
        b"MLCGraph",
        b"nodeWithLayer:sources:disableUpdate:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"MLCInferenceGraph", b"addInputs:", {"retval": {"type": b"Z"}})
    r(
        b"MLCInferenceGraph",
        b"addInputs:lossLabels:lossLabelWeights:",
        {"retval": {"type": b"Z"}},
    )
    r(b"MLCInferenceGraph", b"addOutputs:", {"retval": {"type": b"Z"}})
    r(b"MLCInferenceGraph", b"compileWithOptions:device:", {"retval": {"type": b"Z"}})
    r(
        b"MLCInferenceGraph",
        b"compileWithOptions:device:inputTensors:inputTensorsData:",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MLCInferenceGraph",
        b"executeWithInputsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCInferenceGraph",
        b"executeWithInputsData:lossLabelsData:lossLabelWeightsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                7: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCInferenceGraph",
        b"executeWithInputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                8: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCInferenceGraph",
        b"executeWithInputsData:outputsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(b"MLCInferenceGraph", b"linkWithGraphs:", {"retval": {"type": b"Z"}})
    r(b"MLCLSTMDescriptor", b"batchFirst", {"retval": {"type": b"Z"}})
    r(
        b"MLCLSTMDescriptor",
        b"descriptorWithInputSize:hiddenSize:layerCount:usesBiases:batchFirst:isBidirectional:dropout:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}, 7: {"type": b"Z"}}},
    )
    r(
        b"MLCLSTMDescriptor",
        b"descriptorWithInputSize:hiddenSize:layerCount:usesBiases:batchFirst:isBidirectional:returnsSequences:dropout:",
        {
            "arguments": {
                5: {"type": b"Z"},
                6: {"type": b"Z"},
                7: {"type": b"Z"},
                8: {"type": b"Z"},
            }
        },
    )
    r(
        b"MLCLSTMDescriptor",
        b"descriptorWithInputSize:hiddenSize:layerCount:usesBiases:batchFirst:isBidirectional:returnsSequences:dropout:resultMode:",
        {
            "arguments": {
                5: {"type": "Z"},
                6: {"type": "Z"},
                7: {"type": "Z"},
                8: {"type": "Z"},
            }
        },
    )
    r(
        b"MLCLSTMDescriptor",
        b"descriptorWithInputSize:hiddenSize:layerCount:usesBiases:isBidirectional:dropout:",
        {"arguments": {5: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(b"MLCLSTMDescriptor", b"isBidirectional", {"retval": {"type": b"Z"}})
    r(b"MLCLSTMDescriptor", b"returnsSequences", {"retval": {"type": b"Z"}})
    r(b"MLCLSTMDescriptor", b"usesBiases", {"retval": {"type": b"Z"}})
    r(b"MLCLayer", b"isDebuggingEnabled", {"retval": {"type": b"Z"}})
    r(b"MLCLayer", b"setIsDebuggingEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"MLCLayer", b"supportsDataType:onDevice:", {"retval": {"type": "Z"}})
    r(
        b"MLCMatMulDescriptor",
        b"descriptorWithAlpha:transposesX:transposesY:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type": b"Z"}}},
    )
    r(b"MLCMatMulDescriptor", b"transposesX", {"retval": {"type": b"Z"}})
    r(b"MLCMatMulDescriptor", b"transposesY", {"retval": {"type": b"Z"}})
    r(
        b"MLCMultiheadAttentionDescriptor",
        b"addsZeroAttention",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MLCMultiheadAttentionDescriptor",
        b"descriptorWithModelDimension:keyDimension:valueDimension:headCount:dropout:hasBiases:hasAttentionBiases:addsZeroAttention:",
        {"arguments": {7: {"type": b"Z"}, 8: {"type": b"Z"}, 9: {"type": b"Z"}}},
    )
    r(
        b"MLCMultiheadAttentionDescriptor",
        b"hasAttentionBiases",
        {"retval": {"type": b"Z"}},
    )
    r(b"MLCMultiheadAttentionDescriptor", b"hasBiases", {"retval": {"type": b"Z"}})
    r(b"MLCOptimizer", b"appliesGradientClipping", {"retval": {"type": b"Z"}})
    r(
        b"MLCOptimizer",
        b"setAppliesGradientClipping:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MLCOptimizerDescriptor", b"appliesGradientClipping", {"retval": {"type": b"Z"}})
    r(
        b"MLCOptimizerDescriptor",
        b"descriptorWithLearningRate:gradientRescale:appliesGradientClipping:gradientClipMax:gradientClipMin:regularizationType:regularizationScale:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MLCOptimizerDescriptor",
        b"descriptorWithLearningRate:gradientRescale:appliesGradientClipping:gradientClippingType:gradientClipMax:gradientClipMin:maximumClippingNorm:customGlobalNorm:regularizationType:regularizationScale:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MLCPoolingDescriptor",
        b"averagePoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:countIncludesPadding:",
        {"arguments": {7: {"type": b"Z"}}},
    )
    r(
        b"MLCPoolingDescriptor",
        b"averagePoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:countIncludesPadding:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(b"MLCPoolingDescriptor", b"countIncludesPadding", {"retval": {"type": b"Z"}})
    r(b"MLCRMSPropOptimizer", b"isCentered", {"retval": {"type": b"Z"}})
    r(
        b"MLCRMSPropOptimizer",
        b"optimizerWithDescriptor:momentumScale:alpha:epsilon:isCentered:",
        {"arguments": {6: {"type": b"Z"}}},
    )
    r(
        b"MLCSGDOptimizer",
        b"optimizerWithDescriptor:momentumScale:usesNesterovMomentum:",
        {"arguments": {4: {"type": "Z"}}},
    )
    r(
        b"MLCSGDOptimizer",
        b"optimizerWithDescriptor:momentumScale:usesNestrovMomentum:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"MLCSGDOptimizer", b"usesNesterovMomentum", {"retval": {"type": "Z"}})
    r(b"MLCSGDOptimizer", b"usesNestrovMomentum", {"retval": {"type": b"Z"}})
    r(b"MLCTensor", b"bindAndWriteData:toDevice:", {"retval": {"type": b"Z"}})
    r(b"MLCTensor", b"bindOptimizerData:deviceData:", {"retval": {"type": "Z"}})
    r(
        b"MLCTensor",
        b"copyDataFromDeviceMemoryToBytes:length:synchronizeWithDevice:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type": b"Z"}}},
    )
    r(b"MLCTensor", b"hasValidNumerics", {"retval": {"type": b"Z"}})
    r(b"MLCTensor", b"optimizerData:", {"retval": {"type": b"Z"}})
    r(b"MLCTensor", b"synchronizeData", {"retval": {"type": b"Z"}})
    r(b"MLCTensor", b"synchronizeOptimizerData", {"retval": {"type": "Z"}})
    r(
        b"MLCTensor",
        b"tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:data:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"MLCTensor",
        b"tensorWithSequenceLengths:sortedSequences:featureChannelCount:batchSize:randomInitializerType:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"MLCTensorData", b"bytes", {"retval": {"c_array_of_variable_size": True}})
    r(
        b"MLCTensorData",
        b"dataWithBytesNoCopy:length:",
        {"arguments": {2: {"type_modifier": b"n", "c_array_length_in_arg": 3}}},
    )
    r(
        b"MLCTensorData",
        b"dataWithBytesNoCopy:length:deallocator:",
        {
            "arguments": {
                2: {"type_modifier": b"n", "c_array_length_in_arg": 3},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"n^v", "c_array_length_in_arg": 2},
                            2: {"type": b"Q"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"MLCTensorData",
        b"dataWithImmutableBytesNoCopy:length:",
        {"arguments": {2: {"type_modifier": b"n", "c_array_length_in_arg": 3}}},
    )
    r(
        b"MLCTensorDescriptor",
        b"descriptorWithShape:sequenceLengths:sortedSequences:dataType:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"MLCTensorDescriptor", b"sortedSequences", {"retval": {"type": b"Z"}})
    r(b"MLCTensorParameter", b"isUpdatable", {"retval": {"type": b"Z"}})
    r(b"MLCTensorParameter", b"setIsUpdatable:", {"arguments": {2: {"type": b"Z"}}})
    r(b"MLCTrainingGraph", b"addInputs:lossLabels:", {"retval": {"type": b"Z"}})
    r(
        b"MLCTrainingGraph",
        b"addInputs:lossLabels:lossLabelWeights:",
        {"retval": {"type": b"Z"}},
    )
    r(b"MLCTrainingGraph", b"addOutputs:", {"retval": {"type": b"Z"}})
    r(
        b"MLCTrainingGraph",
        b"bindOptimizerData:deviceData:withTensor:",
        {"retval": {"type": "Z"}},
    )
    r(b"MLCTrainingGraph", b"compileOptimizer:", {"retval": {"type": b"Z"}})
    r(b"MLCTrainingGraph", b"compileWithOptions:device:", {"retval": {"type": b"Z"}})
    r(
        b"MLCTrainingGraph",
        b"compileWithOptions:device:inputTensors:inputTensorsData:",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MLCTrainingGraph",
        b"executeForwardWithBatchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeForwardWithBatchSize:options:outputsData:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeGradientWithBatchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeGradientWithBatchSize:options:outputsData:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeOptimizerUpdateWithOptions:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeWithInputsData:lossLabelsData:lossLabelWeightsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                7: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(
        b"MLCTrainingGraph",
        b"executeWithInputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                8: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"d"},
                        },
                    }
                }
            },
        },
    )
    r(b"MLCTrainingGraph", b"linkWithGraphs:", {"retval": {"type": b"Z"}})
    r(b"MLCTrainingGraph", b"setTrainingTensorParameters:", {"retval": {"type": b"Z"}})
    r(b"MLCTrainingGraph", b"stopGradientForTensors:", {"retval": {"type": b"Z"}})
    r(b"MLCUpsampleLayer", b"alignsCorners", {"retval": {"type": b"Z"}})
    r(
        b"MLCUpsampleLayer",
        b"layerWithShape:sampleMode:alignsCorners:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"MLCYOLOLossDescriptor",
        b"setShouldRescore:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MLCYOLOLossDescriptor", b"shouldRescore", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("MLCOptimizer", b"initWithDescriptor:")
expressions = {}

# END OF FILE
