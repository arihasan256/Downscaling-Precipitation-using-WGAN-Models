import xarray as xr
import numpy as np
import tensorflow as tf
import pandas as pd

def image2Xarray(image, lon, lat, timeSeries):
    """
    Convert an image to an xarray Dataset with optional geographic coordinates
    
    """
    
    # Get image dimensions
    height, width = image.shape[:2]   

    # Create xarray DataArray
    da = xr.DataArray(
        image,
        dims=['time', 'lat', 'lon'],
        coords={
            'time': timeSeries,
            'lat': lat,
            'lon': lon
        },
        name='precipitation'
    )
    
    # Create xarray Dataset
    ds = xr.Dataset({'precipitation': da})
        
    # Add metadata
    ds.attrs['source']  = 'Downscaling'
    ds.attrs['height']  = height
    ds.attrs['width']   = width
    
    ds.attrs['projection'] = 'PlateCarree'  # Assuming simple lat/lon projection
    return ds

def logTransform(data, epsilon=0.1):
    """Apply preprocessing to handle zero-inflation and skewness"""
    # Log transformation with epsilon
    transformed = np.log1p(data + epsilon)
    return transformed

def inverseLogTransform(transformed_data, epsilon=0.1):
    """
    Inverse transform from log1p transformation with epsilon offset
    
    Parameters:
    -----------
    transformed_data : numpy.ndarray or float
        The transformed data (after log1p transform with epsilon)
    epsilon : float
        The small constant added before transformation
        
    Returns:
    --------
    original_data : numpy.ndarray or float
        The original data before transformation
    """
    # Step 1: Reverse the log1p transform using expm1
    intermediate = np.expm1(transformed_data)
    
    # Step 2: Subtract the epsilon that was added
    original_data = intermediate - epsilon
    
    return original_data


def inversTransform(scaler, originalData):
    # Assuming your 4D tensor has shape [batch_size, height, width, channels]
    # and you need to inverse transform it with a scaler

    # Get the original shape
    original_shape = tf.shape(originalData)

    # Reshape to 2D: combine all dimensions except the last one
    # This creates a 2D array of shape [batch_size*height*width, channels]
    reshaped = tf.reshape(originalData, [-1, original_shape[-1]])

    # Convert to numpy for scaler (if needed)
    reshaped_np = reshaped.numpy()

    # Apply inverse transform
    inverse_transformed = scaler.inverse_transform(reshaped_np)

    # Convert back to tensor if needed
    inverse_transformed = tf.convert_to_tensor(inverse_transformed, dtype=originalData.dtype)

    # Reshape back to original 4D shape
    return tf.reshape(inverse_transformed, original_shape)


def selectPrecipitation(dataset, specificDate):
    # Convert the dates to numeric values (nanoseconds since epoch)
    time_values_numeric = dataset.time.values.astype('datetime64[ns]').astype(np.int64)
    specific_date_numeric = specificDate.astype('datetime64[ns]').astype(np.int64)
    
    # Find the index of the closest time
    time_idx = np.abs(time_values_numeric - specific_date_numeric).argmin()
    
    # Use integer indexing to get the data for the closest date
    return dataset['precipitation'].isel(time=time_idx) 

def convertTime(datetime_array):    
    # Store as integer timestamps (nanoseconds since epoch)
    timestamps_ns = np.array([pd.Timestamp(t).value for t in datetime_array], dtype=np.int64)
    return timestamps_ns

def inversTimeFormat(timestamps_ns):
    # Convert nanosecond integers to pandas DatetimeIndex
    datetimes = pd.to_datetime(timestamps_ns, unit='ns')
    
    # Convert to numpy datetime64 array
    datetime64_array = datetimes.to_numpy()
    
    return datetime64_array
    