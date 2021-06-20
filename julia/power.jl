module Power 
export power_method, inverse_power_method

using LinearAlgebra

"""
Calculate the dominant eigenvalue of a matrix A and its associated eigenvector.
"""
function power_method(A::Matrix{<:Real}, x::Vector{<:Real}, n::Int)::Tuple
	y = x
	m = 1

	for _ in 0:n
		y = A * x
		m = maximum(abs.(y))
		x = (m^-1)y
	end

	return (m, y)
end

"""
Calculate the least dominant eigenvalue of a matrix A and its associated
eigenvector.
"""
function inverse_power_method(A::Matrix{<:Real}, x::Vector{<:Real}, n::Int)::Tuple
	return power_method(inv(A), x, n)
end

end
