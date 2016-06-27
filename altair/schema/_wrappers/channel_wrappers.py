# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
import pandas as pd

from ...utils import parse_shorthand, infer_vegalite_type
from ...utils import INV_TYPECODE_MAP, TYPE_ABBR

from .._interface import Type
from .._interface import ChannelDefWithLegend, FieldDef, OrderChannelDef, PositionChannelDef


class PositionChannel(PositionChannelDef):
    """Wrapper for Vega-Lite PositionChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate: AggregateOp
        Aggregation function for the field .
    axis: Union(Bool, Axis)
        
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    scale: Scale
        
    sort: Union(SortField, SortOrder)
        
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Union(Type, Unicode)
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = T.Unicode('')

    # add type abbreviations to the valid values &
    # use an observer below to expand abbreviations if they come up
    type = T.Union([Type(), T.Enum(['Q', 'N', 'O', 'T'])],
                   allow_none=True, default_value=None)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]

    # Class Attributes
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=None, axis=None, bin=None, field=None, scale=None, sort=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(PositionChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])


class ChannelWithLegend(ChannelDefWithLegend):
    """Wrapper for Vega-Lite ChannelDefWithLegend definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate: AggregateOp
        Aggregation function for the field .
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    legend: Legend
        
    scale: Scale
        
    sort: Union(SortField, SortOrder)
        
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Union(Type, Unicode)
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = T.Unicode('')

    # add type abbreviations to the valid values &
    # use an observer below to expand abbreviations if they come up
    type = T.Union([Type(), T.Enum(['Q', 'N', 'O', 'T'])],
                   allow_none=True, default_value=None)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]

    # Class Attributes
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=None, bin=None, field=None, legend=None, scale=None, sort=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, legend=legend, scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(ChannelWithLegend, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])


class Field(FieldDef):
    """Wrapper for Vega-Lite FieldDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate: AggregateOp
        Aggregation function for the field .
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Union(Type, Unicode)
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = T.Unicode('')

    # add type abbreviations to the valid values &
    # use an observer below to expand abbreviations if they come up
    type = T.Union([Type(), T.Enum(['Q', 'N', 'O', 'T'])],
                   allow_none=True, default_value=None)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]

    # Class Attributes
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=None, bin=None, field=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Field, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])


class OrderChannel(OrderChannelDef):
    """Wrapper for Vega-Lite OrderChannelDef definition.
    
    Attributes
    ----------
    shorthand: Unicode
        A shorthand description of the channel
    aggregate: AggregateOp
        Aggregation function for the field .
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    sort: SortOrder
        
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Union(Type, Unicode)
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    # Traitlets
    shorthand = T.Unicode('')

    # add type abbreviations to the valid values &
    # use an observer below to expand abbreviations if they come up
    type = T.Union([Type(), T.Enum(['Q', 'N', 'O', 'T'])],
                   allow_none=True, default_value=None)

    @T.observe('shorthand')
    def _shorthand_changed(self, change):
        D = parse_shorthand(change['new'])
        for key, val in D.items():
            setattr(self, key, val)

    @T.observe('type')
    def _type_changed(self, change):
        new = change['new']
        if new in TYPE_ABBR:
            self.type = INV_TYPECODE_MAP[new]

    # Class Attributes
    skip = ['shorthand']

    # Class Methods
    def __init__(self, shorthand='', aggregate=None, bin=None, field=None, sort=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwargs['shorthand'] = shorthand
        kwds = dict(aggregate=aggregate, bin=bin, field=field, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(OrderChannel, self).__init__(**kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: this involves inferring types if necessary"""
        if self.type is None:
            data = kwargs.get('data', None)
            if isinstance(data, pd.DataFrame) and self.field in data:
                self.type = infer_vegalite_type(data[self.field])


